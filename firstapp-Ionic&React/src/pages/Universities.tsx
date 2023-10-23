import { useState, useEffect } from 'react';
import {
  IonContent,
  IonInfiniteScroll,
  IonInfiniteScrollContent,
  IonItem,
  IonAvatar,
  IonLabel,
  IonGrid,
  IonCol,
  IonRow,
  IonCard,
  IonCardContent,
  IonPage,
  IonHeader,
  IonProgressBar,
  IonSearchbar,
  IonRefresher,
  IonRefresherContent,
  RefresherEventDetail,
  InputChangeEventDetail
}
 from '@ionic/react';
import "../interfaces/Interfaces"

const Universities = () => {
  const [items, setItems] = useState<UniversitiesData[]>([]);
  const [content, setContent] = useState<UniversitiesData[]>([])
  const [country, setCountry] = useState<string>("United States");
  
  const fetchData = async() => {
    
    await fetch("http://universities.hipolabs.com/search?country=" + country.split(" ").join("+"))
      .then(response => {
        return response.json()
      })
      .then(data => {
        setItems(data)
        setContent(data.slice(0,50))
      }).catch(error => console.log('error', error));
      
    }

  const generateItems = () => {
    
    if(items && content.length+50 < items.length){
      setContent([...content, ...items.slice(content.length-1,content.length+50)])
    }
    else{
      setContent([...content, ...items.slice(content.length-1)])
    }
  };
  
  useEffect(() => {  
    generateItems();
  }, []);

  if(items.length==0 && country=="United States"){
    fetchData() 
  }
  

  const SearchF= (value:string) =>{
    if(value == "Enter"){
      setContent([])
      setItems([])
      fetchData()
    }
  }

  const inputHandler = (e:CustomEvent<InputChangeEventDetail>)=>{
    if(e.detail.value){
      setCountry(e.detail.value)
    }else{
      setCountry("United States")
    }
  }

  const handleRefresh = (event: CustomEvent<RefresherEventDetail>) =>{
    setTimeout(() => {
      window.location.reload();
      event.detail.complete();
    }, 2000);
  }
  
  return (
    <IonPage>
      
      <IonHeader>
        <IonSearchbar animated={true} placeholder="Country" onKeyDown={e=> SearchF(e.key)} onIonInput={inputHandler}></IonSearchbar>
      </IonHeader>

      <IonContent>
        <IonRefresher slot="fixed" pullFactor={0.5} pullMin={100} pullMax={200} onIonRefresh={handleRefresh}>
          <IonRefresherContent></IonRefresherContent>
        </IonRefresher>

        <IonGrid>
          <IonRow class="ion-justify-content-center">
            <IonCol size="12" sizeMd="8" sizeLg="6" sizeXl="4">    
          
          {content.length > 0 ? content.map((item: any, index) => (

            <IonCard className='ion-pading' key={index}>
              <IonCardContent>
                <IonItem key={index}>
                  <IonAvatar slot="start">
                    <img src={'https://picsum.photos/80/80?random=' + index} alt="avatar" />
                  </IonAvatar>
                  <IonLabel>{item["name"]}</IonLabel>
                </IonItem>
              </IonCardContent>
            </IonCard>

          )): <IonProgressBar type="indeterminate"></IonProgressBar>}
      
              <IonInfiniteScroll
                onIonInfinite={(ev) => {
                  generateItems();
                  setTimeout(() => ev.target.complete(), 1000);
                }}
              >
                <IonInfiniteScrollContent></IonInfiniteScrollContent>
              </IonInfiniteScroll>
        
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
}
export default Universities;