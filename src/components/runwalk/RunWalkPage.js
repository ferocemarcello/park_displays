import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './RunWalkPage.module.scss';
import data from './data.json';

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
          <div className={styles['ListItem']}>
            <Map bounds={data.waypoints} zoom={15} style={{height: 220, width: 440}} zoomControl={false} doubleClickZoom={false} boxZoom={false} dragging={false} keyboard={false} scrollWheelZoom={false} touchZoom={false}>
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
              <Marker position={[48.161126,11.598448]}>
                <Popup>
                  A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
              </Marker>
              { this.state.line ? <Polyline color="lime" positions={data.waypoints} /> : null }
            </Map>
            <div className={styles['ListItemTextSection']}>
              <div style={{fontSize: '1.5rem', paddingTop: 16}}>Englischer Garten 1</div>
              <div style={{color: 'grey'}}>
                <p>
                <FontAwesomeIcon icon="arrows-alt-h" /> 5,4 km&nbsp;&nbsp;&nbsp;
                <FontAwesomeIcon icon="clock" /> 1:30 h&nbsp;&nbsp;&nbsp;
                <FontAwesomeIcon icon="arrow-up" /> 4 hm&nbsp;&nbsp;&nbsp;
                <FontAwesomeIcon icon="arrow-down" /> 12 hm&nbsp;&nbsp;&nbsp;
                  <FontAwesomeIcon icon="layer-group" /> Gravel
                </p>
                <p style={{fontFamily: 'Helvetica'}}>
                  Hier könnte jetzt noch irgendein Text stehen, der den Nutzer einlädt die Strecke zu laufen.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div className={styles['MapSection']} id="map-section">
          <Map center={centerPosition} zoom={15} style={{height: '100%'}}>
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
            <Marker position={centerPosition}>
              <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
            </Marker>
            { this.state.line ? <Polyline color="lime" positions={data.waypoints} /> : null }
          </Map>
        </div>
      </div>
    )
  }
}

export default RunWalkPage;