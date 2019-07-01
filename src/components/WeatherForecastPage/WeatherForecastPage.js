import React, { Component } from 'react';
import styles from './WeatherForecastPage.module.scss';

class ForecastHour extends Component {
  render() {
    const { date, weather, temp } = this.props;

    const icons = {
      Sunny: 'https://vortex.accuweather.com/adc2010/images/slate/icons/01.svg',
      'Mostly Sunny': 'https://vortex.accuweather.com/adc2010/images/slate/icons/02.svg'
    };

    return (
      <div className={styles['ForecastHour']}>
        <div>
          <small>{date}:00</small>
        </div>
        <img className={styles['WeatherIcon']} src={icons[weather]} />
        <div>
          <div>{weather}</div>
          <div>{temp}°C</div>
        </div>
      </div>
    );
  }
}

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
          <ForecastHour
            date={date.getHours()}
            weather="Sunny"
            temp="29" />
          <ForecastHour
            date={date.getHours() + 1}
            weather="Mostly Sunny"
            temp="29" />
          <ForecastHour
            date={date.getHours() + 2}
            weather="Mostly Sunny"
            temp="30" />
          <ForecastHour
            date={date.getHours() + 3}
            weather="Mostly Sunny"
            temp="30" />
          <ForecastHour
            date={date.getHours() + 4}
            weather="Mostly Sunny"
            temp="30" />
          <ForecastHour
            date={date.getHours() + 5}
            weather="Mostly Sunny"
            temp="30" />
        </section>
      </div>
    )
  }
}

export default WeatherForecastPage;