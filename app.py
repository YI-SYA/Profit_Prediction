# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Model Regresi </h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    Cement = 540
    Blast_slag = 142
    Fly_ash = 163
    Water = 205
    Superplasticizer = 155
    Fine_aggregate = 304
    Age = 14
    Coarse_aggregate = 938
	
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            Cement = st.number_input('Cement', value=Cement)
        with col2:
            Blast_slag = st.number_input('Blast_slag', value=Blast_slag)
        with col3:
            Fly_ash = st.number_input('Fly_ash', value=Fly_ash)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            Water = st.number_input('Water', value=Water)
        with col2:
            Superplasticizer = st.number_input('Superplasticizer', value=Superplasticizer)
        with col3:
            Coarse_aggregate = st.number_input('Coarse_aggregate', value=Coarse_aggregate)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            Fine_aggregate = st.number_input('Fine_aggregate', value=Fine_aggregate)
        with col2:
            Age = st.number_input('Age', value=Age)

    
    st.markdown('---'*10)

    
    data = {
        'Cement': Cement,
        'Blast_slag': Blast_slag,
        'Fly_ash': Fly_ash,
        'Water': Water,
	'Superplasticizer' : Superplasticizer,
	'Coarse_aggregate' : Coarse_aggregate,
	'Fine_aggregate' : Fine_aggregate,
	'Age' : Age,
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('model_oke.pkl', 'rb'))
    
    # Predict
    result = round(float(final_prediction(df_final, my_model)),2)
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Predicted Profit= ', result,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 
