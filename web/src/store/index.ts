import { atom } from 'nanostores';

export const users = atom([
    {
        "name": "Adam",
        "account": 1000000
    },
    {
        "name": "<script>alert('Hello World');</script>",
        "account": 1000000
    }
]);

export const comments = atom([
    {
        "title": "How do I minmax my FOMO",
        "desc": ""
    }
]);