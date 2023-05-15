import { atom } from 'nanostores'
import axios from 'axios'

// export type LoadingStateValue = '' | 'loading' | 'loaded'
export const authenticated = atom<Boolean>(false)
export const token = atom<String>('')
export const profile = atom<Object>({})

export const login = async (username, password) => {
    return await axios({
        method: 'post',
        headers:{"Content-Type": "multipart/form-data"},
        url: "http://localhost:5000/token",
        data:{
            "username": username,
            "password": password
        }

    }).then(response => {
        console.log(response);
        authenticated.set(true);
        token.set(response.data.access_token);
        return true;

    }).catch(error => {
        console.log(error);
        return false;
    });
}

export const hydrate = async () => {
    return await axios({
        method: 'get',
        headers:{"Authorization": `Bearer ${token.value}`},
        url: "http://localhost:5000/hydrate"

    }).then(response => {
        console.log(response)
        profile.set(response.data)
        return true;

    }).catch(error => {
        console.log(error)
        return false;
    });
}