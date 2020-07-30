// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

#include <string.h>

#include <ctype.h>

#include <strings.h>

#include <stdio.h>

#include <stdlib.h>


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26; //N can be changed to so that the hash table contains more buckets

// Hash table
node *table[N];

// Word count

unsigned int wordcount = 0;

// Returns true if word is in dictionary else false. Must be case-insensitive. Should only return TRUE for words in the dictionary.
bool check(const char *word)
{
    // TODO
    unsigned int i = hash(word);
    for (node *cursor = table[i]; cursor != NULL; cursor = cursor->next)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word) //takes a string and returns an index
{
    // TODO
    if (islower(word[0]))
    {
        for (char letter = 'a'; letter <= 'z'; letter++)
        {
            if (word[0] == letter)
            {
                return (letter - 97) % N;
            }
        }
    }
    else if (isupper(word[0]))
    {
        for (char letter = 'A'; letter <= 'Z'; letter++)
        {
            if (word[0] == letter)
            {
                return (letter - 65) % N;
            }
        }
    }
    else
    {
        printf("Invalid word\n");
    }
    return 99;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    //1.Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open dictionary\n");
        return false;
    }
    //2. Read strings from file one at a time

    // Node of size 0, initially not pointing to anything
    node *n = NULL;

    unsigned int i; //index to 'table' array
    char dw[LENGTH + 1]; //create a character array to store a dictionary word

    //For each word in dictionary:
    while (fscanf(file, "%s", dw) != EOF)
    {
        //Keep track of word count
        wordcount++;

        //3. Create a new node
        n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Could not allocate memory for node\n");
            return false;
        }
        strcpy(n->word, dw);
        n->next = NULL;

        //4. Hash word to obtain a new value
        i = hash(dw);
        //5. Insert node into hash table at that location
        if (table[i] == NULL)
        {
            table[i] = n;
        }
        else
        {
            n->next = table[i];
            table[i] = n;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return wordcount;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        // Have cursor point to the node table[i] is pointing to
        node *cursor = table[i];
        while (cursor != NULL)
        {
            // Create another pointer to point to what cursor is pointing to
            node *tmp = cursor;
            // Move cursor to the next node
            cursor = cursor->next;
            // Free the node
            free(tmp);
        }
    }
    return true;
}
