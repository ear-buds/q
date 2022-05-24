import "./PlaylistTable.css";

function PlaylistTable() {
  return (
    <table className="table-auto">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Album</th>
          <th>Date Added</th>
          <th></th>
          <th>Length</th>
        </tr>
      </thead>
    </table>
  );
}

export default PlaylistTable;
