import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'ionic.firstapp',
  appName: 'firstapp',
  webDir: 'dist',
  server: {
    androidScheme: 'https'
  }
};

export default config;
