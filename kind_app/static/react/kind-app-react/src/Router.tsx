import { Home } from '@mui/icons-material';
import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import GratitudeEntryPage from './pages/GratitudeEntryPage';

const Router = createBrowserRouter([
    // {
    //     path: "/",
    //     element: <Home />
    // },
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
    }
]);

export default Router;