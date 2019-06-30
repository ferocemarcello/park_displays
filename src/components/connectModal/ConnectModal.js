import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './ConnectModal.module.scss';

class ConnectModal extends Component {
  render() {
    const { closeConnectModal } = this.props;

    return (
      <div className={styles['modalWrapper']}>
        <div className={styles['background']} onClick={closeConnectModal}></div>
        <div className={styles['modalInner']}>
          <div style={{display: 'flex', marginBottom: 16}}>
            <h2 className={styles['title']}>Connect</h2>
            <div style={{flexGrow: 1}}></div>
            <div onClick={closeConnectModal} className={styles['closeButton']}>
              <FontAwesomeIcon icon="times" />
            </div>
          </div>
          <form>
            <div>
              <input type="text" placeholder="E-Mail"/>
            </div>
            <div>
              <input type="password" placeholder="Password"/>
            </div>
            <button className={styles['socialButton']} style={{marginTop: 0}}>Log In</button>
          </form>
          { /*
          <div style={{marginTop: 10}}>
            <button className={styles['socialButton']}><FontAwesomeIcon icon={['fab', 'strava']} />&nbsp;&nbsp;Login with Strava</button>
            <button className={styles['socialButton']}><FontAwesomeIcon icon={['fab', 'facebook']} />&nbsp;&nbsp;Login with Facebook</button>
            <button className={styles['socialButton']}>Login with Garmin Connect</button>
            <button className={styles['socialButton']}>Login with Polar</button>
          </div>
          */ }
        </div>
      </div>
    );
  }
}

export default ConnectModal;