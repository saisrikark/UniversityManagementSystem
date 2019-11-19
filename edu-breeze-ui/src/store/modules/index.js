import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
import { authentication } from './authReducer';

export default (history) => combineReducers({
  router: connectRouter(history),
  authentication,
})
