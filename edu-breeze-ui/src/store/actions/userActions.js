import { authServices } from './../../services';
import sha256 from 'hash.js/lib/hash/sha/256';
import Cookie from 'js-cookie';

export const userActions = {
    loginAction,
    getUserAction,
};

function loginAction(userCreds, callback) {
    const {
        username,
        password,
    } = userCreds;

    const hashedpassword = sha256().update(password).digest('hex');

    console.log(hashedpassword);

    return dispatch => {
        console.log(userCreds);
        authServices.login(username, hashedpassword)
            .then(resp => {
                if (resp.status === 201 || resp.status === 403) {
                    return resp.json();
                } else {
                    const error = new Error(resp.statusText);
                    error.response = resp;
                    throw error;
                }
            })
            .then(json => {
                console.log('respJsonBody', json);
                Cookie.set('token', json.token, { expires: 1 });
                if (json.login) {
                    dispatch({ type: 'SET_TOKEN_ON_LOGIN', payload: json.token });
                }
                callback(json);
            })
            .catch(error => {
                callback(null, error);
            });
    };
}

function getUserAction(token, callback) {
    return dispatch => {
        console.log(token);

        authServices.getUserByToken(token)
            .then(resp => {
                if (resp.status === 200) {
                    return resp.json();
                } else {
                    const error = new Error(resp.statusText);
                    error.response = resp;
                    throw error;
                }
            })
            .then(json => {
                // Got user document
                dispatch({ type: 'SET_USER', payload: json });
                callback(json);
            })
            .catch(error => callback(null, error));
    }
}