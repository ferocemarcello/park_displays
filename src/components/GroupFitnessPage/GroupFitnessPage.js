import React, { Component } from 'react';
import styles from './GroupFitnessPage.module.scss';
import { Map, Marker, TileLayer } from 'react-leaflet';
import FitnessGroups from '../../data/FitnessGroups';
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

  leafletGroupIcon = icon({
    iconUrl: 'groupicon.png',
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

    return (
      <div className={styles['GroupFitnessPage']}>
        <section className={styles['TextSection']}>
          <h2>Group Fitness</h2>

        </section>

        <Map center={[48.1642323, 11.6033635]} zoom={14} style={{height: 'calc(100vh - 180px)', marginTop: 16}}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          {
            FitnessGroups.map(fitnessGroup => <Marker position={fitnessGroup.location} icon={this.leafletGroupIcon} />)
          }
        </Map>
      </div>
    );
  }
}

export default GroupFitnessPage;