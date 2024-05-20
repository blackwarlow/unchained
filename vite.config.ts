import react from '@vitejs/plugin-react-swc';
import { defineConfig } from 'vite';

// https://vitejs.dev/config/
/** @type {import('vite').UserConfig} */
export default defineConfig({
  root: './',
  publicDir: 'public',
  plugins: [react()],
  resolve: {
    alias: [{ find: '@', replacement: '/frontend' }],
  },
  build: {
    manifest: 'manifest.json',
    copyPublicDir: false,
    outDir: 'build',
    lib: {
      entry: 'frontend/app/index.tsx',
      name: 'frontend',
    },
  },
});
