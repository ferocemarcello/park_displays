import React, { Component } from 'react';
import styles from './WeatherForecastPage.module.scss';

class WeatherForecastPage extends Component {
  render() {
    return (
      <div className={styles['WeatherForecastPage']}>
        WeatherForecast
      </div>
    )
  }
}

export default WeatherForecastPage;