import React, { Component } from 'react';
import data from '../../data.json';
import styles from './TrackDetail.module.scss';
import { Map, Marker, Polyline, Popup, TileLayer } from 'react-leaflet';

class TrackDetail extends Component {
  render() {

    const track = data.filter(track => track.id == this.props.match.params.trackId)[0];

    return (
      <div className={styles['TrackDetailPage']} style={{background: 'url(\'/bg.jpg\') no-repeat center center fixed', backgroundSize: 'cover'}}>
        <section className={styles['TextSection']}>
          <h2>Running & Walking</h2>
          <h1>{track.name}</h1>
        </section>
        <section style={{height: 450}}>
          <Map bounds={track.waypoints} style={{height: 550}}>
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
            <Marker position={track.waypoints[0]} />
            <Polyline color="#006ec0" positions={track.waypoints} />
            {
              track.landmarks.map(landmark =>
                <Marker position={[landmark.lat, landmark.lon]} opacity="0.5">
                  <Popup>
                    {landmark.name}
                  </Popup>
                </Marker>
              )
            }
          </Map>
        </section>
      </div>
    );
  }
}

export default TrackDetail
