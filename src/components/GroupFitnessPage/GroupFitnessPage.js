import React, { Component } from 'react';
import styles from './GroupFitnessPage.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Map, Marker, Polyline, Popup, TileLayer } from 'react-leaflet';
import Landmarks from '../../data/Landmarks';
import { icon } from 'leaflet';

class GroupFitnessPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      filterSectionExpanded: false,
      gymTools: {
        smithMachine: true,
        airWalker: true,
        rower: true,
        weightBench: true
      }
    };
  }

  leafletGymtoolIcon = icon({
    iconUrl: 'gymtool.png',
    iconSize: [32, 32]
  });

  handleGymtoolFilterChange = (evt) => {
    const { value } = evt.target;

    this.setState(prevState => ({
      ...prevState,
      gymTools: {
        ...prevState.gymTools,
        [value]: !prevState.gymTools[value]
      }
    }));
  };

  toggleFilterSection = () => {
    this.setState((prevState) => ({
      ...prevState,
      filterSectionExpanded: !prevState.filterSectionExpanded
    }));
  };

  gymToolFilter = (gymTool) => {
    const selectedGymTools = Object.keys(this.state.gymTools).filter(gymTool => this.state.gymTools[gymTool]);
    return selectedGymTools.includes(gymTool.type);
  };

  render() {
    const { filterSectionExpanded } = this.state;

    const gymTools = Landmarks.gymtools.filter(gymTool => this.gymToolFilter(gymTool));

    return (
      <div className={styles['GroupFitnessPage']}>
        <section className={styles['TextSection']}>
          <h2>Group Fitness</h2>

        </section>
        <div className={styles['FilterSectionHeader']} onClick={this.toggleFilterSection}>
          <div style={{float: 'left'}}>Filter Gym Machine Types</div>
          <div style={{float: 'right'}}>
            <FontAwesomeIcon icon={filterSectionExpanded ? 'caret-up' : 'caret-down'} />
          </div>
        </div>
        <div className={styles['FilterSectionBody']} style={{height: this.state.filterSectionExpanded ? 50 : 0, padding: this.state.filterSectionExpanded ? 16 : null}}>
          <table className={styles['FilterTable']}>
            <tbody>
            <tr>
              <td scope="row">Machine Types</td>
              <td>
                <input type="checkbox" name="gymTool" value="smithMachine" checked={this.state.gymTools.smithMachine} onChange={this.handleGymtoolFilterChange} /> Smith Machine&nbsp;&nbsp;
                <input type="checkbox" name="gymTool" value="airWalker" checked={this.state.gymTools.airWalker} onChange={this.handleGymtoolFilterChange} /> Air Walker&nbsp;&nbsp;
                <input type="checkbox" name="gymTool" value="rower" checked={this.state.gymTools.rower} onChange={this.handleGymtoolFilterChange} /> Rower&nbsp;&nbsp;
                <input type="checkbox" name="gymTool" value="weightBench" checked={this.state.gymTools.weightBench} onChange={this.handleGymtoolFilterChange} /> Weight Bench&nbsp;&nbsp;
              </td>
            </tr>
            </tbody>
          </table>
        </div>

        <Map center={[48.1642323, 11.6033635]} zoom={14} style={{height: 'calc(100vh - 250px)', marginTop: 16}}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          {
            gymTools.map((gymTool, index) => (
              <Marker position={gymTool.location} icon={this.leafletGymtoolIcon} key={index}>
                <Popup>
                  {gymTool.name.replace('\\', '').replace('\\', '')}
                </Popup>
              </Marker>
            ))
          }
        </Map>
      </div>
    );
  }
}

export default GroupFitnessPage;