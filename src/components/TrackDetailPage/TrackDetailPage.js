import React, { Component } from 'react';
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import data from '../../data/RunWalkData.json';
import styles from './TrackDetailPage.module.scss';
import { Map, Marker, Polyline, Popup, TileLayer } from 'react-leaflet';
import QRCodeGenerator from 'qrcode-generator';
import { icon } from 'leaflet';

class TrackDetailPage extends Component {

  leafletMonumentIcon = icon({
    iconUrl: 'monument_icon.png',
    iconSize: [32, 32]
  });

  render() {

    const track = data.filter(track => track.id == this.props.match.params.trackId)[0];

    const qrCode = QRCodeGenerator(4, 'H');
    qrCode.addData('https://www.google.com');
    qrCode.make();

    return (
      <div className={styles['TrackDetailPage']}>
        <section className={styles['TextSection']}>
          <h2>Running & Walking</h2>
          <h1>{track.name}</h1>
          {<div dangerouslySetInnerHTML={{ __html: qrCode.createSvgTag() }}></div>}
          <div style={{display: 'flex', height: 200}}>
            <table className={styles['DetailTable']}>
              <tbody>
              <tr>
                <td scope="row">Distance</td>
                <td>1.6 km</td>
              </tr>
              <tr>
                <td scope="row">Duration</td>
                <td>1:20 h</td>
              </tr>
              <tr>
                <td scope="row">Ascent</td>
                <td>12 m</td>
              </tr>
              <tr>
                <td scope="row">Descent</td>
                <td>12 m</td>
              </tr>
              </tbody>
            </table>
            <HighchartsReact style={{flex: '1 0 50%'}}
                             highcharts={Highcharts}
                             options={{
                               chart: {
                                 type: 'area',
                                 animation: false,
                                 backgroundColor: 'rgba(0,0,0,0)'
                               },
                               title: {
                                 text: 'Height Profile'
                               },
                               series: [{
                                 name: 'Elevation',
                                 data: track.waypointElevation,
                                 color: '#006ec0'
                               }],
                               tooltip: {
                                 enabled: false
                               },
                               legend: {
                                 enabled: false
                               },
                               xAxis: {
                                 visible: false
                               },
                               yAxis: {
                                 title: {
                                   text: 'Meters'
                                 }
                               },
                               credits: false
                             }}
            />
          </div>
        </section>
        <section style={{height: 450}}>
          <Map bounds={track.waypoints} style={{height: 550}}>
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' />
            <Marker position={track.waypoints[0]} />
            <Polyline color="#006ec0" positions={track.waypoints} />
            {
              track.landmarks.map((landmark, index) =>
                <Marker position={[landmark.lat, landmark.lon]} opacity="0.9" icon={this.leafletMonumentIcon} key={index}>
                  <Popup>
                    {landmark.name.replace('\\', '').replace('\\', '')}
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

export default TrackDetailPage
