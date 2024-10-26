import streamlit as st
import requests
import os

os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

BASE_URL = "http://127.0.0.1:8000"  # URL da sua API FastAPI


def fetch_teams():
    response = requests.get(f"{BASE_URL}/teams/")
    return response.json()


def fetch_players(team_id):
    response = requests.get(f"{BASE_URL}/teams/{team_id}/players")
    return response.json()


def main():
    st.title("Campeonato do Brasileirão 2024 - Série A")

    # Exibir todos os times
    st.header("Times")
    teams = fetch_teams()
    team_names = [team['name'] for team in teams]

    selected_team = st.selectbox("Selecione um time", team_names)

    # Mostrar informações do time selecionado
    if selected_team:
        team = next((team for team in teams if team['name'] == selected_team), None)
        if team:
            st.subheader(f"Time: {team['name']}")
            st.write(f"Classificação: {team['rank']}")

            # Obter e mostrar os jogadores do time
            players = fetch_players(team['id'])
            st.subheader("Jogadores")
            for player in players:
                st.write(f"Nome: {player['name']}")
    else:
        st.write("Nenhum time disponível.")

if __name__ == "__main__":
    main()
