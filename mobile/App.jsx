import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { AppRegistry, StyleSheet, Text, View, TextInput, Button } from 'react-native';



export default class App extends Component {

    constructor() {
        super();

        this.state = {
            address: '',
            fetched_data: [],
            loadingState: 1
        }
        
    }
    
    handlePress() {
        this.getArticles();
    };

    exit() {
        this.setState({ loadingState: 1 })
    }

    async getArticles() {
        await fetch(this.state.address, {method: 'GET'})
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({ loadingState: 2, fetched_data: data })
            })
            .catch(err => {
                console.error(err);
                this.setState({ loadingState: 3 })
            });

    }


    render() {
        if (this.state.loadingState === 1) {
            return (<View style={styles.container}>
                <Text></Text>
                <Text></Text>
                <TextInput
                    placeholder="Enter ip and port, ex: 10.10.10.1:80"
                    returnKeyLabel={"next"}
                    onChangeText={(text) => this.setState({ address: 'http://' + text })}
                />
                <Button title="Send request" onPress={this.handlePress.bind(this)} />
                <StatusBar style="auto" />
            </View>);
        }

        else if (this.state.loadingState === 2) {
            return (
                //warning: for now showing fetched_data is hardcoded, this is for change when json keys specified
                <View style={styles.container}>
                    <Text>Temperature: {this.state.fetched_data.temperature}</Text>
                    <Text>Humidity: {this.state.fetched_data.humidity}</Text>
                    <Text>Pressure: {this.state.fetched_data.pressure}</Text>
                    <Text></Text>
                    <Button title="Go back" onPress={this.exit.bind(this)} />
                    <Button title="Refresh" onPress={this.handlePress.bind(this)} />
                </View>
            );
        }
        else {
            return (
                <View style={styles.container}>
                    <Text>Sorry, something went wrong, try again</Text>
                    <Text></Text>
                    <Button title="Try again" onPress={this.exit.bind(this)} />
                </View>

            );
        }
   
    }
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});