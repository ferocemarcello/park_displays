import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './ConnectModal.module.scss';

class ConnectModal extends Component {
  render() {
    const { closeConnectModal } = this.props;

    return (
      <div className={styles['modalWrapper']}>
        <div className={styles['modalInner']}>
          <div style={{display: 'flex', marginBottom: 16}}>
            <h2 style={{margin: 0}}>Connect</h2>
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
            <button>Log In</button>
          </form>
          <div>
            <button>Social 1</button>
          </div>
        </div>
      </div>
    );
  }
}

export default ConnectModal;