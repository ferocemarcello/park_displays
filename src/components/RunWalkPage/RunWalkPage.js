import React, { Component } from 'react';
import { Map, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './RunWalkPage.module.scss';
import data from '../../data.json';

class TrackListItem extends Component {
  render() {
    const { trackId, trackName, trackDistance, trackDuration, trackUp, trackDown, trackGroundType, trackAnnotation, waypoints } = this.props;
    return (
      <Link to={`/runwalk/track/${trackId}`} className={styles['ListItem']}>
        <Map bounds={waypoints} zoom={15} style={{height: 220, width: 440}} zoomControl={false} doubleClickZoom={false} boxZoom={false} dragging={false} keyboard={false} scrollWheelZoom={false} touchZoom={false}>
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
    console.log(data);
    const { filterSectionExpanded } = this.state;

    return (
      <div className={styles['RunWalkPage']} style={{background: 'url(\'/bg.jpg\') no-repeat center center fixed', backgroundSize: 'cover'}}>
        <div className={styles['TextSection']} id="textSection">
          <h1>Running & Walking</h1>
        </div>
        <div className={styles['FilterSectionHeader']} onClick={this.toggleFilterSection}>
          <div style={{float: 'left'}}>Filter Running & Walking Tracks</div>
          <div style={{float: 'right'}}>
            <FontAwesomeIcon icon={filterSectionExpanded ? 'caret-up' : 'caret-down'} />
          </div>
        </div>
        <div className={styles['FilterSectionBody']} style={{height: this.state.filterSectionExpanded ? 150 : 0, padding: this.state.filterSectionExpanded ? 16 : null}}>
          <p>
            <span>Distance</span>
            <span>
              <input type="range" min="0" max="100" />
            </span>
          </p>
          <p>
            <span>Duration</span>
            <span>
              <input type="range" min="0" max="100" />
            </span>
          </p>
          <p>
            <span>Height Difference</span>
            <span>
              <input type="range" min="0" max="100" />
            </span>
          </p>
          <p>
            <span>Ground Type</span>
            <span>
              <input type="checkbox" name="groundType" /> Gravel
              <input type="checkbox" name="groundType" /> Grass
              <input type="checkbox" name="groundType" /> Asphalt
            </span>
          </p>
        </div>
        <div className={styles['ListSection']}>
          {
            data.map((track) =>
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
      </div>
    )
  }
}

export default RunWalkPage;