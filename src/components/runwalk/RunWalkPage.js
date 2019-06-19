import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './RunWalkPage.module.scss';
import data from './data.json';

class TrackListItem extends Component {
  render() {
    const { trackId, trackName, trackDistance, trackDuration, trackUp, trackDown, trackGroundType, trackAnnotation, waypoints } = this.props;
    return (
      <Link to={`/runwalk/track/${trackId}`} className={styles['ListItem']}>
        <Map bounds={waypoints} zoom={15} style={{height: 220, width: 440}} zoomControl={false} doubleClickZoom={false} boxZoom={false} dragging={false} keyboard={false} scrollWheelZoom={false} touchZoom={false}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          <Marker position={[48.161126,11.598448]}>
            <Popup>
              A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
          </Marker>
          <Polyline color="lime" positions={waypoints} />
        </Map>
        <div className={styles['ListItemTextSection']}>
          <div className={styles['ListItemTextSectionTitle']}>{trackName}</div>
          <div className={styles['ListItemTextSectionBody']}>
            <p>
              <FontAwesomeIcon icon="arrows-alt-h" /> {trackDistance}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="clock" /> {trackDuration}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-up" /> {trackUp}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-down" /> {trackDown}&nbsp;&nbsp;&nbsp;
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

class RunWalkPage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      filterSectionExpanded: false,
      line: true
    };
  }

  toggleFilterSection = () => {
    this.setState((prevState) => ({
      ...prevState,
      filterSectionExpanded: !prevState.filterSectionExpanded
    }));
  };

  toggleLine = () => {
    this.setState((prevState) => ({
      ...prevState,
      line: !prevState.line
    }));
  }

  componentDidMount() {
    /*global $:true*/
    $('#map-section').css('height', window.innerHeight - $('#appToolbar').height() - $('#textSection').height());
  }


  render() {
    const centerPosition = [48.148673, 11.589373];

    console.log(data);

    return (
      <div className={styles['RunWalkPage']} style={{background: 'url(\'/bg.jpg\') no-repeat center center fixed', backgroundSize: 'cover'}}>
        <div className={styles['TextSection']} id="textSection">
          <h1>Running & Walking</h1>
          RunWalkPage
          <div style={{}}>Filter Section Header <button onClick={this.toggleFilterSection}>Toggle</button> <button onClick={this.toggleLine}>Toggle Line</button></div>
          <div style={{height: this.state.filterSectionExpanded ? 250 : 0, overflow: 'hidden', transition: 'height 0.5s ease-in-out'}}>
            Filter Section
          </div>
        </div>
        <div className={styles['ListSection']}>
          <TrackListItem
            trackId="00001"
            trackName="Englischer Garten 1"
            trackDistance="5.4 km"
            trackDuration="1:30 h"
            trackUp="4 hm"
            trackDown="12 hm"
            trackGroundType="Gravel"
            trackAnnotation="Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen."
            waypoints={data.waypoints} />

          <TrackListItem
            trackId="00001"
            trackName="Englischer Garten 2"
            trackDistance="5.4 km"
            trackDuration="1:30 h"
            trackUp="4 hm"
            trackDown="12 hm"
            trackGroundType="Gravel"
            trackAnnotation="Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen."
            waypoints={data.waypoints} />

          <TrackListItem
            trackId="00001"
            trackName="Englischer Garten 3"
            trackDistance="5.4 km"
            trackDuration="1:30 h"
            trackUp="4 hm"
            trackDown="12 hm"
            trackGroundType="Gravel"
            trackAnnotation="Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen."
            waypoints={data.waypoints} />

          <TrackListItem
            trackId="00001"
            trackName="Englischer Garten 4"
            trackDistance="5.4 km"
            trackDuration="1:30 h"
            trackUp="4 hm"
            trackDown="12 hm"
            trackGroundType="Gravel"
            trackAnnotation="Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen."
            waypoints={data.waypoints} />

          <TrackListItem
            trackId="00001"
            trackName="Englischer Garten 5"
            trackDistance="5.4 km"
            trackDuration="1:30 h"
            trackUp="4 hm"
            trackDown="12 hm"
            trackGroundType="Gravel"
            trackAnnotation="Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen."
            waypoints={data.waypoints} />
        </div>
      </div>
    )
  }
}

export default RunWalkPage;