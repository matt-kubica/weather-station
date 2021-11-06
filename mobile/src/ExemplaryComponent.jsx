import React from 'react';
import { Text } from 'react-native';

export const ExemplaryComponent = ({text}) => {
    return (
        <Text>Hello form exemplary component! This is text passed as a prop: {text}</Text>
    );
}