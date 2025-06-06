'use client';


import { useState } from 'react';


// A simple SVG spinner component
const Spinner = () => (
  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
  </svg>
);


export default function Home() {
  const [url, setUrl] = useState('');
  const [html, setHtml] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!url || isLoading) return;


    setIsLoading(true);
    setHtml('');
    setError('');


    try {
      const res = await fetch('http://127.0.0.1:8000/clone', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });


      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }


      const data = await res.json();
      setHtml(data.cloned_html);
    } catch (err) {
      console.error("Cloning failed:", err);
      setError(err instanceof Error ? err.message : 'An unknown error occurred. Please check the backend console.');
      setHtml(''); // Clear any previous successful clones
    } finally {
      setIsLoading(false);
    }
  };


  return (
    <div className="flex flex-col items-center min-h-screen bg-gray-900 text-white font-sans p-4 sm:p-6 md:p-8">
      <div className="w-full max-w-4xl">
        {/* Header Section */}
        <header className="text-center mb-10">
          <h1 className="text-4xl sm:text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
            Orchids AI Website Cloner
          </h1>
          <p className="text-gray-400 mt-2 text-lg">
            An AI that clones the aesthetics of any given website.
          </p>
        </header>


        {/* Input Form */}
        <form onSubmit={handleSubmit} className="mb-10">
          <div className="flex flex-col sm:flex-row gap-4">
            <input
              type="url"
              placeholder="https://example.com"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              disabled={isLoading}
              className="flex-grow bg-gray-800 border border-gray-700 text-gray-200 rounded-lg px-4 py-3 focus:ring-2 focus:ring-purple-500 focus:outline-none transition-all duration-300 disabled:opacity-50"
              required
            />
            <button
              type="submit"
              disabled={isLoading}
              className="flex items-center justify-center bg-purple-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-purple-700 active:bg-purple-800 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-900 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-purple-900/40"
            >
              {isLoading ? (
                <>
                  <Spinner />
                  Cloning...
                </>
              ) : 'Clone Website'}
            </button>
          </div>
        </form>


        {/* Cloned Preview Section */}
        <div className="w-full">
          <h2 className="text-2xl font-semibold mb-4 text-gray-300">Cloned Preview</h2>
          <div className="bg-gray-800 rounded-xl border border-gray-700 shadow-2xl shadow-black/30 overflow-hidden min-h-[500px]">
            {error && (
              <div className="p-8 text-center text-red-400">
                <h3 className="text-xl font-bold mb-2">An Error Occurred</h3>
                <p className="text-red-300 bg-red-900/30 p-4 rounded-lg">{error}</p>
              </div>
            )}
            {html && !error && (
              <iframe
                srcDoc={html}
                className="w-full h-[60vh] min-h-[500px] border-0"
                sandbox="allow-scripts" // Allow scripts for potential edge cases, but our prompt forbids them
              />
            )}
             {!html && !error && (
                <div className="flex items-center justify-center h-[500px] text-gray-500">
                    <p>The cloned website preview will appear here.</p>
                </div>
            )}
          </div>
        </div>
       
        {/* Footer */}
        <footer className="text-center mt-12 text-gray-500">
            <p>Built for the Orchids SWE Internship Challenge.</p>
        </footer>
      </div>
    </div>
  );
}
