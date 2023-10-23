import { useState } from 'react';

import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonItem,
  IonLabel,
  IonList,
  useIonActionSheet ,
  IonButton,
  useIonAlert,
  IonIcon,
  IonAlert
} from '@ionic/react';

import { closeSharp } from 'ionicons/icons';
import "../interfaces/Interfaces"

const Population = () => {

  const [data, setData] = useState<PopulationData[]>([]);
  const [presentAlert] = useIonAlert();
  const [present] = useIonActionSheet();
  const [trigger, setTrigger] = useState<boolean>(false)
  

  const fetchData = async() => {
    
    await fetch("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    .then(response => response.json())
    .then(result=>setData(result.data))
    .catch(error => console.log('error', error));

  }
  
  if(data.length==0){
    fetchData()
  }

  const clickHandler = (action:string, year:string)=>{
    if(action=="Delete"){
      const copy: PopulationData[] = [...data]
      let result = copy.filter((item:any)=>item["Year"]!=year)
      setData([...result])
    }
  }

  const addHandler = (year:string, population: number)=>{
    if(year!="" && population>0){
      let copy: PopulationData = JSON.parse(JSON.stringify(data[0]))
      copy["Year"] = year;
      copy["Population"] = population;
      setData([copy, ...data])
    }
    else{
     setTrigger(!trigger)
    }

  }

  return (
    
    
    <IonCard>
      <IonCardHeader>
        <IonCardTitle>United States</IonCardTitle>
        <IonCardSubtitle>Population</IonCardSubtitle>
        <IonButton
      onClick={() =>
        presentAlert({
          header: 'Enter info:',
          buttons: [
            {
              text: 'Add',
              cssClass: 'alert-button-confirm',
              handler: (inputs)=>addHandler(inputs.Year, inputs.Population)
            }
          ],
          inputs: [
            {
              type: "number",
              placeholder: 'Year',
              name: "Year",
            },
            {
              type: "number",
              placeholder: 'Population',
              name: "Population"
            
            },
            
          ],
        })
      }
    >
      Add new!
        </IonButton>
      </IonCardHeader>
      
      <IonAlert
        isOpen={trigger}
        onDidDismiss={() => setTrigger(!trigger)}
        header={"Alert"}
        message={'All fields are required!'}
        buttons={['OK']}
      >
      </IonAlert>

      <IonCardContent>
        <IonList>
         
          {data && data.map((item,index)=>(
            <IonItem key={item["Year"]}>
              <IonLabel>Year: {item["Year"]} Population: {item["Population"]}</IonLabel>
              <IonButton key={item["Year"]} size='small' fill='clear' color={'danger'}
               onClick={() =>
                present({
                  header: "Delete "+item["Year"] ,
                  cssClass: 'my-custom-class',
                  buttons: [
                    {
                      text: 'Delete',
                      role: 'destructive',
                      handler: () => clickHandler('Delete', item["Year"]),
                      data: {
                        action: 'delete',
                      },

                    },
                    {
                      text: 'Cancel',
                      role: 'cancel',
                      data: {
                        action: 'cancel',
                      },
                    },
                  ],
                })
                }
              >
                <IonIcon icon={closeSharp}></IonIcon>
              </IonButton>
            </IonItem>
          ))}
          
        </IonList>
        
      </IonCardContent>
    </IonCard>
    
  );
}

export default Population;