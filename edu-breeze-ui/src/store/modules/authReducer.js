import Cookie from 'js-cookie';

const token = Cookie.get('token');
console.log(token);
const initialState = token ? { loggedIn: true, token }: { loggedIn: false };

export function authentication(state = initialState, action) {
    console.log(action)
    switch(action.type) {
        case "SET_TOKEN_ON_LOGIN":
            return {
                loggedIn: true,
                token: action.payload,
            };
        case "SET_USER":
            return {
                ...state,
                user: action.payload,
            };
        default:
            return state;
    }
}