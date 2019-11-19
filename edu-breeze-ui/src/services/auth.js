import 'whatwg-fetch';

import { apiMicroservices } from './apiMicroservices.js';

export const authServices = {
    login,
    logout,
    // checkUserName,
    getUserByToken,
    isLoggedIn,
}

const userendpoints = {
    isLoggedIn: apiMicroservices.userMs + '/token/isLoggedIn',
    getUserByToken: apiMicroservices.userMs + '/users/getUserByToken',
    login: apiMicroservices.userMs + '/login',
    logout: apiMicroservices.userMs + '/logout',
};

function login(username, password) {
    return fetch(userendpoints.login, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username,
            password,
        }),
    });
}

function logout(token, callback) {
    return fetch(userendpoints.logout, {
        method: 'DELETE',
    });
}

function getUserByToken(token, callback) {
    return fetch(userendpoints.getUserByToken + '?token=' + token)
}

function isLoggedIn(token, callback) {
    return fetch(userendpoints.isLoggedIn + '?token=' + token);
}
