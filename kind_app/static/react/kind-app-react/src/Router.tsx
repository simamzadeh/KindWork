import { createBrowserRouter } from 'react-router-dom';
import SatisfactionPage from './pages/SatisfactionPage';
import KudosPage from './pages/KudosPage';
import AchievementPage from './pages/AchievementPage';

// Login, logout and registration pages are not included in the Router as they use Bootstrap instead
const Router = createBrowserRouter([
    {
        path: "kudos/",
        element:<KudosPage />
    },
    {
        path: "achievements/",
        element:<AchievementPage />
    },
    {
        path: "satisfaction/",
        element:<SatisfactionPage />
    }
]);

export default Router;