import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { AppRegistry, StyleSheet, Text, View, TextInput, Button } from 'react-native';

export default class App extends Component {

    constructor() {
        super();
        this.state = {
            ip: '',
            fetched_data: [],
            isLoading: false,
        }
        
    }
    
    handlePress() {
        let examples = this.getArticles();
    };

    exit() {
        this.setState({ isLoading:false })
    }

    async getArticles() {
        await fetch(this.state.ip, {method: 'GET'})
            .then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({ isLoading: true, fetched_data: data })
            })
            .catch(err => console.error(err));

    }


    render() {
        if (!this.state.isLoading) {
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

        else {
            return (
                //warning: for now showing fetched_data is hardcoded, this is for change when json keys specified
                <View style={styles.container}>
                <Text>{this.state.fetched_data.date}</Text>
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