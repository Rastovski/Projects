import { IonList, IonContent, IonHeader, IonMenu, IonLabel, IonItem, IonTitle, IonToolbar } from '@ionic/react';
const Toolbar = () => {
  return (
    <>
      <IonMenu contentId="main">
        <IonHeader>
          <IonToolbar>
            <IonTitle>USA</IonTitle>
          </IonToolbar>
        </IonHeader>

        <IonContent className="ion-padding">
          <IonList>
            
            <IonItem routerLink="/population">
              <IonLabel>Population</IonLabel>
            </IonItem>

            <IonItem routerLink="/universities">
              <IonLabel>Universities</IonLabel>
            </IonItem>

          </IonList>
        </IonContent>

      </IonMenu>
    </>
  );
}
export default Toolbar;