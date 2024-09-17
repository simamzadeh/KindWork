import { Home } from '@mui/icons-material';
import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import GratitudeEntryPage from './pages/GratitudeEntryPage';
import HomePage from './pages/HomePage';
import KindActPage from './pages/KindActPage';

const Router = createBrowserRouter([
    {
        path: "/",
        element: <HomePage />
    },
    // {
    //     path: "login/",
    //     element <Login />
    // }
    // {
    //     path: "register/",
    //     element: <Registration />
    // }
    {
        path: "gratitude/",
        element:<GratitudeEntryPage />
    },
    {
        path: "kind-acts/",
        element:<KindActPage />
    }
]);

export default Router;