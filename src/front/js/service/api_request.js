const URL = "https://3001-m4n50n-jwtauthenticati-unefitvx3h1.ws-eu32.gitpod.io"; // Without '/' at the end!

// Fetch functions definition
export const ApiUserRegister = (userCredentials) =>
    fetch(`${URL}/api/user/register`, {
        method: "POST",
        body: JSON.stringify(userCredentials)
    });

export const ApiUserLogin = (userCredentials) =>
    fetch(`${URL}/api/user/login`, {
        method: "POST",
        body: JSON.stringify(userCredentials)
    });

export const ApiUserValidation = () =>
    fetch(`${URL}/api/user/validate`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("api-flask-token"),
        }
    });

export const ApiUserLogout = () => localStorage.removeItem("api-flask-token");
