import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup } from 'react-leaflet';
import styles from './ParkMapPage.module.scss';

class ParkMapPage extends Component {
  render() {
    return (
      <div className={styles['ParkMapPage']}>
        ParkMapPage
        <Map center={[48.112824, 11.6295388]} zoom={15} style={{height: 400}}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
          <Marker position={[48.112824, 11.6295388]}>
            <Popup>
              A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
          </Marker>
        </Map>
      </div>
    )
  }
}

export default ParkMapPage;