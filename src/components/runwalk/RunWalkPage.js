import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
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