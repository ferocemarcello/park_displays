import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './ToolBarItem.module.scss';

class BackToolbarItem extends Component {
  render() {
    return (
      <a className={styles['ToolBarItem']} href="#" onClick={this.props.history.goBack}>
        <span className={styles['ToolBarItemIcon']}>
          <FontAwesomeIcon icon="arrow-left" />
        </span>
      </a>
    )
  }
}

export default BackToolbarItem;