function Logo(props) {
  return (
    <svg width={`${props.width}px`} height={`${props.height}px`} viewBox="0 0 800 600" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" xmlSpace="preserve" xmlnserif="http://www.serif.com/" style={{fillRule:"evenodd", clipRule:"evenodd", strokeLinejoin:"round", strokeMiterlimit:2}}>
      <g>
          <g transform="matrix(1.86916,0,0,1.86916,-47.6636,39.2523)">
              <path d="M239.5,-21C328.082,-21 400,50.918 400,139.5C400,228.082 328.082,300 239.5,300C150.918,300 79,228.082 79,139.5C79,50.918 150.918,-21 239.5,-21ZM239.5,19.125C305.937,19.125 359.875,73.063 359.875,139.5C359.875,205.937 305.937,259.875 239.5,259.875C173.063,259.875 119.125,205.937 119.125,139.5C119.125,73.063 173.063,19.125 239.5,19.125Z" style={{ fill:props.color }}/>
          </g>
          <path d="M700,543.75C700,533.402 691.598,525 681.25,525L418.75,525C408.402,525 400,533.402 400,543.75L400,581.25C400,591.598 408.402,600 418.75,600L681.25,600C691.598,600 700,591.598 700,581.25L700,543.75Z" style={{fill:props.color}}/>
      </g>
    </svg>
  );
}

export default Logo;
