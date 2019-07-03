import React, { Component } from 'react';
import styles from './SimillarUsersPage.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Map, Marker, Polyline, Popup, TileLayer } from 'react-leaflet';
import Landmarks from '../../data/Landmarks';
import { icon } from 'leaflet';

class SimillarUsersPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      filterSectionExpanded: false,
      activities: {
        running: true,
        walking: true,
        bodyweight: true,
        gym: true
      }
    };
  }

  leafletGymtoolIcon = icon({
    iconUrl: 'gymtool.png',
    iconSize: [32, 32]
  });

  handleActivityFilterChange = (evt) => {
    const { value } = evt.target;

    this.setState(prevState => ({
      ...prevState,
      activities: {
        ...prevState.activities,
        [value]: !prevState.activities[value]
      }
    }));
  };

  toggleFilterSection = () => {
    this.setState((prevState) => ({
      ...prevState,
      filterSectionExpanded: !prevState.filterSectionExpanded
    }));
  };

  activityFilter = (activity) => {
    const selectedActivities = Object.keys(this.state.activities).filter(activity => this.state.activities[activity]);
    return selectedActivities.includes(activity.type);
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
                <input type="checkbox" name="activity" value="running" checked={this.state.activities.running} onChange={this.handleActivityFilterChange} /> Running&nbsp;&nbsp;
                <input type="checkbox" name="activity" value="walking" checked={this.state.activities.walking} onChange={this.handleActivityFilterChange} /> Walking&nbsp;&nbsp;
                <input type="checkbox" name="activity" value="bodyweight" checked={this.state.activities.bodyweight} onChange={this.handleActivityFilterChange} /> Bodyweight&nbsp;&nbsp;
                <input type="checkbox" name="activity" value="gym" checked={this.state.activities.gym} onChange={this.handleActivityFilterChange} /> Outdoor Gym&nbsp;&nbsp;
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

export default SimillarUsersPage;