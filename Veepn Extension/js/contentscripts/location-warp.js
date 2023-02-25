// eslint-disable-next-line func-names
const processLocationWarp = function (conf) {
  return `
   window.spC1337 = 1;
  (function() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition = function(success) { if(success) { setTimeout(function(){success(${conf})},1000); } return };
      navigator.geolocation.watchPosition = function(success) { spC1337++; if(success) { setTimeout(function(){success(${conf})},1000); } return spC1337; };
    } else {
      console.error('Geolocation is not supported in this browser');
    }
  })()
`;
};

chrome.runtime
  .sendMessage({ request: 'LocationWarp' }, (response) => {
    // json from state, contains current data center location, proxy must be ON
    if (response) {
      const script = document.createElement('script');
      script.textContent = processLocationWarp(response);
      document.documentElement.appendChild(script);
      script.remove();
    }
  });
