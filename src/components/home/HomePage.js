import React, { Component } from 'react';
import styles from './HomePage.module.scss';
import ConnectModal from '../connectModal/ConnectModal';

class HomePage extends Component {
  render() {
    return (
      <div className={styles['HomePage']}>
        <section className={styles['RunningSection']}>
          <div className={styles['SectionTitle']}>Running / Walking</div>
          <div className={styles['SectionDescription']}>Routes for walking</div>
        </section>
        <section className={styles['BodyweightSection']}>
          <div className={styles['SectionTitle']}>Bodyweight</div>
          <div className={styles['SectionDescription']}>Einzigartige Workouts</div>
        </section>
        <section className={styles['GymSection']}>
          <div className={styles['SectionTitle']}>Gym</div>
          <div className={styles['SectionDescription']}>Workouts with equipment</div>
        </section>
        <section>
          Nutrition
        </section>
        <ConnectModal />
      </div>
    )
  }
}

export default HomePage;