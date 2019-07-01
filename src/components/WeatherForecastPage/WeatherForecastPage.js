import React, { Component } from 'react';
import styles from './WeatherForecastPage.module.scss';

class WeatherForecastPage extends Component {
  render() {
    const date = new Date();

    return (
      <div className={styles['WeatherForecastPage']}>
        <section className={styles['TextSection']}>
          <h2>Weather Forecast</h2>
          <h1>Munich - Englischer Garten</h1>
        </section>
        <section className={styles['HourlyForecastSection']}>
          <div className={styles['ForecastHour']}>
            Forecast 1
          </div>
        </section>
      </div>
    )
  }
}

export default WeatherForecastPage;