import "./PlaylistTable.css";

function PlaylistTable() {
  return (
    <div className="table">
      <div className="table-column">#</div>
      <div className="table-column">Name</div>
      <div className="table-column">Album</div>
      <div className="table-column">Date Added</div>
      <div className="table-column"></div>
      <div className="table-column">Length</div>
    </div>
  );
}

export default PlaylistTable;
