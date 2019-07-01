import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';
import styles from './ParkMapPage.module.scss';
import Landmarks from '../../data/Landmarks';
import { icon } from 'leaflet';

class ParkMapPage extends Component {


  leafletMonumentIcon = icon({
    iconUrl: 'monument_icon.png',
    iconSize: [32, 32]
  });

  leafletWaterIcon = icon({
    iconUrl: 'water.png',
    iconSize: [32, 32]
  });

  leafletGymtoolIcon = icon({
    iconUrl: 'gymtool.png',
    iconSize: [32, 32]
  });


  render() {

    return (
      <div className={styles['ParkMapPage']}>
        <Map center={[48.1642323, 11.6033635]} zoom={14} style={{height: 'calc(100vh - 96px)'}}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          {
            Landmarks.fountains.map((landmark, index) =>
              <Marker position={landmark.location} opacity="0.9" icon={this.leafletWaterIcon} key={index} />
            )
          }

          {
            Landmarks.gymtools.map((landmark, index) =>
              <Marker position={landmark.location} opacity="0.9" icon={this.leafletGymtoolIcon} key={index}>
                <Popup>
                  {landmark.name.replace('\\', '').replace('\\', '')}
                </Popup>
              </Marker>
            )
          }
        </Map>
      </div>
    )
  }
}

export default ParkMapPage;