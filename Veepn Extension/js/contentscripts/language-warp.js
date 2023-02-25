// eslint-disable-next-line func-names
const processLanguageWarp = function (locale) {
  return `(() => {
    Object.defineProperties(Navigator.prototype, {
      language: {
        value: '${locale}',
        configurable: false,
        enumerable: true,
        writable: false
      },
      languages: {
        value: ['${locale}'],
        configurable: false,
        enumerable: true,
        writable: false
      }
    });
  })();`;
};

chrome.runtime
  .sendMessage({ request: 'LanguageWarp' }, (response) => {
    if (response) {
      const script = document.createElement('script');
      script.textContent = processLanguageWarp(response);
      document.documentElement.appendChild(script);
      script.remove();
    }
  });
