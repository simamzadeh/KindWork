import { createBrowserRouter } from 'react-router-dom';
import GratitudeEntryPage from './pages/GratitudeEntryPage';
import KindActPage from './pages/KindActPage';
import SatisfactionPage from './pages/SatisfactionPage';

// Login, logout and registration pages are not included in the Router as they use Bootstrap instead
const Router = createBrowserRouter([
    {
        path: "/",
        element: <GratitudeEntryPage />
    },
    {
        path: "gratitude/",
        element:<GratitudeEntryPage />
    },
    {
        path: "kind-acts/",
        element:<KindActPage />
    },
    {
        path: "satisfaction/",
        element:<SatisfactionPage />
    }
]);

export default Router;