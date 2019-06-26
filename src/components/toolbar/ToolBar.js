import React, { Component } from 'react';
import './ToolBar.scss';
import ToolBarItem from '../toolbar-item/ToolBarItem';
import BackToolbarItem from '../toolbar-item/BackToolbarItem';
import ClickToolbarItem from '../toolbar-item/ClickToolbarItem';

class ToolBar extends Component {
  render() {
    const { showConnectModal } = this.props;

    return (
      <div className="toolbar" id="appToolbar">
        {
          //<BackToolbarItem history={this.props.history} />
        }
        <ToolBarItem text="Home" icon="home" to="/" />
        <ToolBarItem text="Emergency" icon="medkit" to="/emergency" />
        <ToolBarItem text="Park Map" icon="map" to="/map" />
        <ToolBarItem text="Weather Forecast" icon="sun" to="/weather" />
        <ClickToolbarItem text="Connect" icon="user-circle" onClick={showConnectModal} />
      </div>
    )
  }
}

export default ToolBar;