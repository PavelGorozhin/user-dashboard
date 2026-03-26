// types.ts

// Import type definitions
import { User } from './user.model';

// Define type aliases
type DashboardType = 'home' | 'settings' | 'account';

// Define interface for dashboard item
interface DashboardItem {
  id: string;
  name: string;
  type: DashboardType;
}

// Define interface for user dashboard
interface UserDashboard {
  dashboardItems: DashboardItem[];
  user: User;
}

// Define type for error
interface Error {
  message: string;
  statusCode: number;
}