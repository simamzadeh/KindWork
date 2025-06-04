import { createBrowserRouter } from 'react-router-dom';
import KindActPage from './pages/KindActPage';
import SatisfactionPage from './pages/SatisfactionPage';
import KudosPage from './pages/KudosPage';

// Login, logout and registration pages are not included in the Router as they use Bootstrap instead
const Router = createBrowserRouter([
    {
        path: "kudos/",
        element:<KudosPage />
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