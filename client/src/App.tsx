import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Compliance from "./pages/Compliance";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Process from "./pages/Process";
import Records from "./pages/Records";
import MentorProfile from "./pages/MentorProfile";
import Appointments from "./pages/Appointments";

function Router() {
  return <Switch><Route path="/" component={Home} /><Route path="/process" component={Process} /><Route path="/compliance" component={Compliance} /><Route path="/records" component={Records} /><Route path="/appointments" component={Appointments} /><Route path="/mentors/:slug" component={MentorProfile} /><Route path="/404" component={NotFound} /><Route component={NotFound} /></Switch>;
}

export default function App() {
  return <ErrorBoundary><ThemeProvider defaultTheme="light"><TooltipProvider><Toaster position="top-center" richColors /><Router /></TooltipProvider></ThemeProvider></ErrorBoundary>;
}
