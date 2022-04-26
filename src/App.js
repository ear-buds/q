import "./App.css";

import SideMenu from "./components/side-menu/SideMenu";
import PlaylistTable from "./components/playlist-table/PlaylistTable";
import PlaylistDetail from "./components/playlist-detail/PlaylistDetail";

function App() {
  return (
    <div className="App">
      <SideMenu />
      <PlaylistDetail />
      <PlaylistTable />
    </div>
  );
}

export default App;
