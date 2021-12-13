import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { AppRegistry, StyleSheet, Text, View, TextInput, Button } from 'react-native';



export default class App extends Component {

    constructor() {
        super();

        this.state = {
            ip: '',
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
        await fetch(this.state.ip, {method: 'GET'})
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
                    placeholder="Enter IP, ex: htttp://date.jsontest.com"
                    returnKeyLabel={"next"}
                    onChangeText={(text) => this.setState({ ip: text })}
                />
                <Button title="Send request" onPress={this.handlePress.bind(this)} />
                <StatusBar style="auto" />
            </View>);
        }

        else if (this.state.loadingState === 2) {
            return (
                //warning: for now showing fetched_data is hardcoded, this is for change when json keys specified
                <View style={styles.container}>
                    <Text>{this.state.fetched_data.date}</Text>
                    <Text></Text>
                    <Button title="<" onPress={this.exit.bind(this)} />
                </View>
            );
        }
        else {
            return (
                <View style={styles.container}>
                    <Text>Sorry, something went wrong, try again</Text>
                    <Text></Text>
                    <Button title="<" onPress={this.exit.bind(this)} />
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