import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './RunWalkPage.module.scss';
import data from '../../data/RunWalkData.json';
import Landmarks from '../../data/Landmarks';

class TrackListItem extends Component {
  render() {
    const { trackId, trackName, trackDistance, trackDuration, trackUp, trackDown, trackGroundType, trackAnnotation, waypoints } = this.props;
    return (
      <Link to={`/runwalk/track/${trackId}`} className={styles['ListItem']}>
        <Map bounds={waypoints} zoom={15} style={{height: 220, width: 300, flexShrink: 0}} zoomControl={false} doubleClickZoom={false} boxZoom={false} dragging={false} keyboard={false} scrollWheelZoom={false} touchZoom={false}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          <Marker position={waypoints[0]} />
          <Polyline color="#006ec0" positions={waypoints} />
        </Map>
        <div className={styles['ListItemTextSection']}>
          <div className={styles['ListItemTextSectionTitle']}>{trackName}</div>
          <div className={styles['ListItemTextSectionBody']}>
            <p>
              <FontAwesomeIcon icon="arrows-alt-h" /> {trackDistance}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="clock" /> {trackDuration}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-up" /> {trackUp}m&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-down" /> {trackDown}m&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="layer-group" /> {trackGroundType}
            </p>
            <p className={styles['ListItemTextSectionDescription']}>
              {trackAnnotation}
            </p>
          </div>
        </div>
      </Link>
    );
  }
}

class RecommendationModal extends Component {
  render() {
    const { hideModal } = this.props;

    return (
      <div className={styles['RecommendationModalWrapper']}>
        <div className={styles['RecommendationModalOuter']}>
          <div className={styles['RecommendationModalInner']}>
            <h3>Get Recommendations</h3>
            <table className={styles['FilterTable']}>
              <tbody>
              <tr>
                <td scope="row">Gender</td>
                <td>
                  <select name="gender">
                    <option value="F">Female</option>
                    <option value="M">Male</option>
                    <option value="D">Diverse</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td scope="row">Age</td>
                <td>
                  <select name="age">
                    <option value="F">Female</option>
                    <option value="M">Male</option>
                    <option value="D">Diverse</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td scope="row">Weight</td>
                <td>
                  <select name="weight">
                    <option value="F">Female</option>
                    <option value="M">Male</option>
                    <option value="D">Diverse</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td scope="row">Kcal</td>
                <td>
                  <select name="energy">
                    <option value="F">Female</option>
                    <option value="M">Male</option>
                    <option value="D">Diverse</option>
                  </select>
                </td>
              </tr>
              </tbody>
            </table>
            <button className={styles['PrimaryButton']} style={{margin: 16, width: 'calc(100% - 32px)'}}>Get Recommendations</button>
          </div>
        </div>
        <div className={styles['RecommendationModalBackground']} onClick={hideModal}></div>
      </div>
    );
  }
}

class RunWalkPage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      showRecommendationSettingsModal: false,
      filterSectionExpanded: false,
      mapView: false,
      groundTypes: {
        gravel: true,
        grass: true,
        asphalt: true
      },
      duration: 120,
      distance: 5000,
      hightDifference: 50
    };
  }

  toggleFilterSection = () => {
    this.setState((prevState) => ({
      ...prevState,
      filterSectionExpanded: !prevState.filterSectionExpanded
    }));
  };

  toggleGroundType = (evt) => {
    const { value } = evt.target;

    this.setState((prevState) => ({
      ...prevState,
      groundType: {
        ...prevState.groundTypes,
        [value]: !prevState.groundTypes[value]
      }
    }));
  };

  groundTypeFilter = (track) => {
    const selectedTypes = Object.keys(this.state.groundTypes)
      .filter(groundType => this.state.groundTypes[groundType])
      .map(groundType => groundType.toUpperCase());

    return selectedTypes.includes(track.groundType);
  };

  durationFilter = (track) => {
    return this.state.duration >= track.duration
  };

  distanceFilter = (track) => {
    return this.state.distance >= track.distance;
  };

  heightDifferenceFilter = (track) => {
    return this.state.hightDifference >= track.heightDifferenceUp;
  };

  formatDuration = (durationInMinutes) => {
    const hours = Math.floor(durationInMinutes / 60);
    const minutes = durationInMinutes - hours * 60;

    if (hours > 0 && minutes === 0) {
      return `${hours}h`;
    }

    if (hours > 0) {
      return `${hours}h ${minutes}min`;
    }

    return `${minutes}min`;
  };

  formatDistance = (distanceInMeters) => {
    const kilometers = Math.floor(distanceInMeters / 1000);
    const meters = distanceInMeters - kilometers * 1000;

    if (kilometers > 0 && meters === 0) {
      return `${kilometers}km`;
    }

    if (kilometers > 0) {
      if (meters < 100)
        return `${kilometers},${Math.round(meters / 10)}km`;
      if (meters < 1000)
        return `${kilometers},${Math.round(meters / 100)}km`;
    }

    return `${meters}m`;
  };

  toggleMapView = () => {
    this.setState(prevState => ({
      ...prevState,
      mapView: !prevState.mapView
    }));
  };

  handleGroundTypeFilterChange = (evt) => {
    const { value } = evt.target;

    this.setState(prevState => ({
      ...prevState,
      groundTypes: {
        ...prevState.groundTypes,
        [value]: !prevState.groundTypes[value]
      }
    }));
  };

  handleRangeChange = (evt) => {
    const { name, value } = evt.target;

    this.setState(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  showRecommendationSettingsModal = () => {
    this.setState(prevState => ({
      ...prevState,
      showRecommendationSettingsModal: true
    }));
  };

  hideRecommendationSettingsModal = () => {
    this.setState(prevState => ({
      ...prevState,
      showRecommendationSettingsModal: false
    }));
  };


  render() {
    const { filterSectionExpanded, showRecommendationSettingsModal } = this.state;

    const tracks = data.filter(track => this.durationFilter(track))
      .filter(track => this.distanceFilter(track))
      .filter(track => this.heightDifferenceFilter(track))
      .filter(track => this.groundTypeFilter(track));

    return (
      <div className={styles['RunWalkPage']}>
        <div className={styles['TextSection']} id="textSection">
          <h1>Running & Walking</h1>
        </div>
        <div className={styles['FilterSectionHeader']} onClick={this.toggleFilterSection}>
          <div style={{float: 'left'}}>Filter Running & Walking Tracks</div>
          <div style={{float: 'right'}}>
            <FontAwesomeIcon icon={filterSectionExpanded ? 'caret-up' : 'caret-down'} />
          </div>
        </div>
        <div className={styles['FilterSectionBody']} style={{height: this.state.filterSectionExpanded ? 260 : 0, padding: this.state.filterSectionExpanded ? 16 : null}}>
          <table className={styles['FilterTable']}>
            <tbody>
            <tr>
              <td scope="row">Distance ({this.formatDistance(this.state.distance)})</td>
              <td><input type="range" min="0" max="10000" step="100" name="distance" value={this.state.distance} onChange={this.handleRangeChange} /></td>
            </tr>
            <tr>
              <td scope="row">Duration ({this.formatDuration(this.state.duration)})</td>
              <td><input type="range" min="1" max="360" name="duration" value={this.state.duration} onChange={this.handleRangeChange} /></td>
            </tr>
            <tr>
              <td scope="row">Height Difference  ({this.formatDistance(this.state.hightDifference)})</td>
              <td><input type="range" min="0" max="500" step="10" name="hightDifference" value={this.state.hightDifference} onChange={this.handleRangeChange} /></td>
            </tr>
            <tr>
              <td scope="row">Ground Type</td>
              <td>
                <input type="checkbox" name="groundType" value="gravel" checked={this.state.groundTypes.gravel} onChange={this.handleGroundTypeFilterChange} /> Gravel&nbsp;&nbsp;
                <input type="checkbox" name="groundType" value="grass" checked={this.state.groundTypes.grass} onChange={this.handleGroundTypeFilterChange} /> Grass&nbsp;&nbsp;
                <input type="checkbox" name="groundType" value="asphalt" checked={this.state.groundTypes.asphalt} onChange={this.handleGroundTypeFilterChange} /> Asphalt&nbsp;&nbsp;
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div>
          {//<button className={styles['PrimaryButton']} style={{margin: 16}} onClick={this.showRecommendationSettingsModal}>Get Recommendations</button>
          }
          <button className={styles['PrimaryButton']} style={{margin: 16, float: 'right'}} onClick={this.toggleMapView}>{ this.state.mapView ? <span>View as List</span> : <span>View as Map</span> }</button>
        </div>

        {
          this.state.mapView ?
            <Map center={[48.1642323, 11.6033635]} zoom={14} style={{height: 'calc(100vh - 96px)'}}>
              <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
              {
                tracks.map((track, index) =>
                  <>
                    <Marker position={track.waypoints[0]} key={index}>
                      <Popup>
                        {track.name.replace('\\', '').replace('\\', '')}
                      </Popup>
                    </Marker>
                    <Polyline color="#006ec0" positions={track.waypoints} />
                  </>
                )
              }
            </Map>
            :
            <div className={styles['ListSection']}>
              {
                tracks
                  .map((track) =>
                    <TrackListItem
                      trackId={track.id}
                      trackName={track.name}
                      trackDistance={track.distance}
                      trackDuration={track.duration}
                      trackUp={track.heightDifferenceUp}
                      trackDown={track.heightDifferenceDown}
                      trackGroundType={track.groundType}
                      trackAnnotation={track.annotation}
                      waypoints={track.waypoints}
                    />
                  )
              }
            </div>
        }
        { showRecommendationSettingsModal ? <RecommendationModal hideModal={this.hideRecommendationSettingsModal} /> : null }
      </div>
    )
  }
}

export default RunWalkPage;