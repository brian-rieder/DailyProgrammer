// Author: Brian Rieder
// Title: Get Your Priorities Right!
// Link: http://www.reddit.com/r/dailyprogrammer/comments/2vkwgb/20150211_challenge_201_practical_exercise_get/

// Specification
// Your priority queue must implement at least these methods:
// Enqueue. This method accepts three parameters - a string, priority value A, and priority value B, where the priority 
//    values are real numbers (see above). The string is inserted into the priority queue with the given priority values A 
//    and B (how you store the queue in memory is up to you!)
// DequeueA. This method removes and returns the string from the priority queue with the highest priority A value. If two 
//    entries have the same A priority, return whichever was enqueued first.
// DequeueB. This method removes and returns the string from the priority queue with the highest priority B value. If two 
//    entries have the same B priority, return whichever was enqueued first.
// Count. This method returns the number of strings in the queue.
// Clear. This removes all entries from the priority queue.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct dpq_t {
	char* name;
	float priorityValA;
	float priorityValB;
	struct dpq_t* next;
} DualPriorityQueue;

typedef struct dpq_meta_t {
	DualPriorityQueue* dpq_by_a;
	DualPriorityQueue* dpq_by_b;
} DPQMeta;

void DPQPrint(DualPriorityQueue* dpq)
{
    if (dpq != NULL) {
        printf("%s \n", dpq->name);
        DPQPrint(dpq->next);
    }
}

DPQMeta* DPQMetaConstruct() {
	DPQMeta* ret = malloc(sizeof(DPQMeta));
	ret->dpq_by_a = NULL;
	ret->dpq_by_b = NULL;
	return ret;
}

DualPriorityQueue* DPQConstruct(char* name, float priorityValA, float priorityValB) {
	DualPriorityQueue * retdpq = malloc(sizeof(DualPriorityQueue));
	retdpq->name = strdup(name);
	retdpq->priorityValA = priorityValA;
	retdpq->priorityValB = priorityValB;
	return retdpq;
}

void DPQEnqueue(DPQMeta* dpq_meta, char* name, float priorityValA, float priorityValB) {
	int go_on_flag = 0;
	if(dpq_meta->dpq_by_a == NULL && dpq_meta->dpq_by_b == NULL) {
		dpq_meta->dpq_by_a = DPQConstruct(name, priorityValA, priorityValB);
		dpq_meta->dpq_by_b = DPQConstruct(name, priorityValA, priorityValB);
		return;
	}

	DualPriorityQueue* appendage_1 = DPQConstruct(name, priorityValA, priorityValB);

	DualPriorityQueue* itr = dpq_meta->dpq_by_a;
	if(itr->priorityValA < priorityValA) {
		appendage_1->next = itr;
		dpq_meta->dpq_by_a = appendage_1;
		go_on_flag = 1;
	}
	if(!go_on_flag) {
		while(itr->next != NULL) {
			if(itr->next->priorityValA > priorityValA) itr = itr->next;
			else break;
		}
		appendage_1->next = itr->next;
		itr->next = appendage_1;
	}

	DualPriorityQueue* appendage_2 = DPQConstruct(name, priorityValA, priorityValB);
	go_on_flag = 0;
	itr = dpq_meta->dpq_by_b;
	if(itr->priorityValB < priorityValB) {
		appendage_2->next = itr;
		dpq_meta->dpq_by_b = appendage_2;
	}
	if(!go_on_flag) {
		while(itr->next != NULL) {
			if(itr->next->priorityValB > priorityValB) itr = itr->next;
			else break;
		}
		appendage_2->next = itr->next;
		itr->next = appendage_2;
	}
}

char* DPQDequeueA(DPQMeta* dpq_meta) {
	DualPriorityQueue* itr = dpq_meta->dpq_by_a;
	char* retstr = NULL;
	if(itr == NULL) return "empty queue";
	if(itr->next == NULL) retstr = itr->name;
	if(retstr == NULL) {
		while(itr->next->next != NULL) itr = itr->next;
		// we have second to last element in itr
		retstr = strdup(itr->next->name);
		free(itr->next->name);
		free(itr->next);
		itr->next = NULL;
	}
	itr = dpq_meta->dpq_by_b;
	while(strcmp(itr->next->name, retstr) != 0) itr = itr->next;
	// itr->next is the node
	DualPriorityQueue* tmp = itr->next;
	itr->next = itr->next->next;
	free(tmp->name);
	free(tmp);
	return retstr;
}

char* DPQDequeueB(DPQMeta* dpq_meta) {
	DualPriorityQueue* itr = dpq_meta->dpq_by_b;
	char* retstr = NULL;
	if(itr == NULL) return "empty queue";
	if(itr->next == NULL) retstr = itr->name;
	if(retstr == NULL) {
		while(itr->next->next != NULL) itr = itr->next;
		// we have second to last element in itr
		retstr = strdup(itr->next->name);
		free(itr->next->name);
		free(itr->next);
		itr->next = NULL;
	}
	itr = dpq_meta->dpq_by_a;
	while(strcmp(itr->next->name, retstr) != 0) itr = itr->next;
	// itr->next is the node
	DualPriorityQueue* tmp = itr->next;
	itr->next = itr->next->next;
	free(tmp->name);
	free(tmp);
	return retstr;
}

void DPQClear(DPQMeta* meta) { //destructor
	DualPriorityQueue* dpq_a = meta->dpq_by_a;
	DualPriorityQueue* dpq_b = meta->dpq_by_b;
	DualPriorityQueue* tmp_a = meta->dpq_by_a->next;
	DualPriorityQueue* tmp_b = meta->dpq_by_b->next;
	while(dpq_a != NULL && dpq_b != NULL) {
		free(dpq_a->name);
		free(dpq_b->name);
		free(dpq_a);
		free(dpq_b);
		dpq_a = dpq_a->next;
		dpq_b = dpq_b->next;
		if(dpq_a->next == NULL) {
			if(dpb_b == NULL || dpq_b->next != NULL) {
				printf("queue mismatch");
				return;
			}
			return;
		}
		tmp_a = dpq_a->next;
		tmp_b = dpq_b->next;
	}
}

int DPQCount(DPQMeta* meta) {
	int count = 0;
	DualPriorityQueue* dpq = meta->dpq_by_a;
	while(dpq != NULL) {
		++count;
		dpq = dpq->next;
	} 	
	return count;
}

int main(int argc, char** argv)
{
	DPQMeta meta;
	meta.dpq_by_a = NULL;
	meta.dpq_by_b = NULL;

	DPQEnqueue(&meta, "reddit", 2, 1);
	DPQClear(meta.dpq_by_a);
	return 0;
}
