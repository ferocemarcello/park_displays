import React, { Component } from 'react';
import styles from './SimillarUsersPage.module.scss';
import { Map, Marker, TileLayer } from 'react-leaflet';
import SportingAthletes from '../../data/SportingAtheles';
import { icon } from 'leaflet';

class SimillarUsersPage extends Component {
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

  leafletBodyweightIcon = icon({
    iconUrl: 'freeweighticon.png',
    iconSize: [32, 32]
  });

  leafletRunningIcon = icon({
    iconUrl: 'runningicon.png',
    iconSize: [32, 32]
  });

  leafletWalkingIcon = icon({
    iconUrl: 'walkingicon.png',
    iconSize: [32, 32]
  });

  leafletStretchingIcon = icon({
    iconUrl: 'stretchingicon.png',
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

  renderSportingAthlete = (athleteObject) => {
    switch (athleteObject.type) {
      case 'RUNNING':
        return <Marker position={athleteObject.location} icon={this.leafletRunningIcon} />;
      case 'WALKING':
        return <Marker position={athleteObject.location} icon={this.leafletWalkingIcon} />;
      case 'GYM':
        return <Marker position={athleteObject.location} icon={this.leafletGymtoolIcon} />;
      case 'BODYWEIGHT':
        return <Marker position={athleteObject.location} icon={this.leafletBodyweightIcon} />;
      case 'STRETCHING':
        return <Marker position={athleteObject.location} icon={this.leafletStretchingIcon} />;
    }
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
            SportingAthletes.map(this.renderSportingAthlete)
          }
        </Map>
      </div>
    );
  }
}

export default SimillarUsersPage;